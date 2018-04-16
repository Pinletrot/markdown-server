import axios from 'axios';
import { cleanAuthor, xpathMatch, xpathText } from './utils';

class PaperItem {
    public title: string = '';
    public url: string = '';
    public pdfUrl: string = '';
    public date: string = '';
    public authors: string[] = [];
}

const translators: Array<(doc: Document, url: string) => Promise<PaperItem>> = [];

function registerTranslator(translator: (doc: Document, url: string) => Promise<PaperItem>) {
    translators.push(translator);
}

async function translate(url: string) {
    const response = await axios.get(url);
    const doc = new DOMParser().parseFromString(response.data, 'text/html');

    let ret;
    for (const translator of translators) {
        try {
            ret = ret || await translator(doc, url);
        } finally {
            // ;
        }
    }
    if (ret === undefined || ret.title === undefined) {
        return new PaperItem();
    }

    return ret;
}

async function parse(doc: Document, url: string) {
    const regexs = [
        new RegExp('https?://arxiv\\.org/'),
        new RegExp('https?://openreview\\.net/'),
        new RegExp('https?://papers\\.nips\\.cc/'),
        new RegExp('https?://(doi|dl)\\.acm\\.org'),
        new RegExp('https?://proceedings\\.mlr\\.press'),
    ];

    const item = new PaperItem();
    let find = false;
    for (const regex of regexs) {
        if (regex.test(url)) {
            find = true;
            break;
        }
    }
    if (!find) {
        return item;
    }

    item.url = url;
    item.title = xpathText(doc, '//head/meta[@name="citation_title"]');
    item.pdfUrl = xpathText(doc, '//head/meta[@name="citation_pdf_url"][1]');
    item.date = xpathText(doc, '//head/meta[@name="citation_publication_date"]')
        || xpathText(doc, '//head/meta[@name="citation_online_date"]')
        || xpathText(doc, '//head/meta[@name="citation_date"]');

    for (const node of xpathMatch(doc, '//head/meta[@name="citation_author"]')) {
        item.authors.push(cleanAuthor((node as any).content, 'author', false));
    }
    // doi.acm.org has an attribute of 'citation_authors' instead of 'citation_author'
    if (url.indexOf('acm.org') !== -1) {
        const authors = xpathText(doc, '//head/meta[@name="citation_authors"]') as string;
        for (let author of authors.split(';')) {
            author = author.trim();
            const names = author.split(',', 2);
            item.authors.push(cleanAuthor((names[1] + ' ' + names[0]), 'author', false));
        }
    }

    return item;
}

registerTranslator(parse);

export {
    translate,
};
