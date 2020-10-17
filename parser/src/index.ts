import { createServer, Server } from 'http';
import { config } from 'dotenv'; config();

import { parserRequest } from './parserRequest';

const { PORT } = process.env;

const server: Server = createServer(parserRequest);

server.listen(PORT, () => {
    console.log(`server has started on ${PORT} port.`);
});
