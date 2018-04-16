import { registerTranslator } from './index';
import { cleanAuthor, PaperItem, xpathMatch, xpathText } from './utils';

async function parse(doc: Document, url: string) { // : Promise<PaperItem> {
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
