export class PaperItem {
    public title: string = '';
    public url: string = '';
    public pdfUrl: string = '';
    public date: string = '';
    public authors: string[] = [];
}

export function xpathText(doc: Document | Node, expr: string, ns?: any, delimiter?: string) {
    const result: any[] = xpathMatch(doc, expr, ns);
    const strings = [];
    for (const node of result) {
        if (node.nodeType === 2 && 'value' in node) {
            strings.push(node.value);
        } else if ('content' in node) {
            strings.push(node.content);
        } else if ('textContent' in node) {
            strings.push(node.textContent);
        } else if ('text' in node) {
            strings.push(node.text);
        } else {
            strings.push(node.nodeValue);
        }
    }
    return strings.join(delimiter || ',');
}

export function xpathMatch(doc: Document | Node, expr: string, ns?: any): Node[] {
    let resolver: any;
    if (ns) {
        resolver = (prefix: string) => ns[prefix] || null;
    }
    const results = document.evaluate(expr, doc, resolver, 5, null);
    const ret = [];
    for (let node; ;) {
        node = results.iterateNext();
        if (!node) { break; }
        ret.push(node);
    }
    return ret;
}

export function cleanAuthor(author: string, type: string, useComma?: boolean): string {
    const allCaps = 'A-Z' + '\u0400-\u042f';		// cyrilic

    const allCapsRe = new RegExp('^[' + allCaps + ']+$');
    const initialRe = new RegExp('^-?[' + allCaps + ']$');

    if (typeof (author) !== 'string') {
        throw new Error('cleanAuthor: author must be a string');
    }

    author = author.replace(/^[\s\u00A0\.\,\/\[\]\:]+/, '')
        .replace(/[\s\u00A0\.\,\/\[\]\:]+$/, '').replace(/[\s\u00A0]+/, ' ');

    let lastName: string = '';
    let firstName: string = '';
    if (useComma) {
        // Add spaces between periods
        author = author.replace(/\.([^ ])/, '. $1');

        const splitNames = author.split(/, ?/);
        if (splitNames.length > 1) {
            lastName = splitNames[0];
            firstName = splitNames[1];
        } else {
            lastName = author;
        }
    } else {
        // Don't parse'Firstname Lastname [Country]'as'[Country], Firstname Lastname'
        let spaceIndex = author.length;
        do {
            spaceIndex = author.lastIndexOf(' ', spaceIndex - 1);
            lastName = author.substring(spaceIndex + 1);
            firstName = author.substring(0, spaceIndex);
        } while (false);
        // } while (!RegExp('\\pL').test(lastName[0]) && spaceIndex > 0); // TODO: replace RegExp by XRegExp
    }

    if (firstName && allCapsRe.test(firstName) && firstName.length < 4 &&
        (firstName.length === 1 || lastName.toUpperCase() !== lastName)) {
        // first name is probably initials
        let newFirstName = '';
        for (const ch of firstName) {
            newFirstName += ' ' + ch + '.';
        }
        firstName = newFirstName.substr(1);
    }

    // add periods after all the initials
    if (firstName) {
        const names = firstName.replace(/^[\s\.]+/, '')
            .replace(/[\s\,]+$/, '')
            // remove spaces surronding any dashes
            .replace(/\s*([\u002D\u00AD\u2010-\u2015\u2212\u2E3A\u2E3B])\s*/, '-')
            .split(/(?:[\s\.]+|(?=-))/);
        let newFirstName = '';
        for (let i = 0, n = names.length; i < n; i++) {
            newFirstName += names[i];
            if (initialRe.test(names[i])) { newFirstName += '.'; }
            newFirstName += ' ';
        }
        firstName = newFirstName.replace(/ -/g, '-').trim();
    }

    return firstName + ', ' + lastName;
}
