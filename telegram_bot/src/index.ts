import { Telegraf } from 'telegraf';

import helpController from './controllers/help';
import startController from './controllers/start';
import stopController from './controllers/stop';

const bot = new Telegraf(process.env.TELEGRAM_TOKEN as string);

// bot.use(Telegraf.log());

bot.command('start', startController);
bot.command('stop', stopController);
bot.command('help', helpController);

bot.launch();
