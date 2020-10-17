import { IncomingMessage, ServerResponse } from "http";

export function parserRequest(req: IncomingMessage, res: ServerResponse) {
    res.statusCode = 200;
    res.end('LOL');
}
