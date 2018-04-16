import axios from 'axios';
import { PaperItem } from './utils';

const translators: Array<(doc: Document, url: string) => Promise<PaperItem>> = [];

function registerTranslator(translator: (doc: Document, url: string) => Promise<PaperItem>) {
    translators.push(translator);
}

async function translate(url: string) { // : Promise<PaperItem> {
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

export {
    registerTranslator,
    translate,
};

declare var require: any;
require('./meta.ts');
