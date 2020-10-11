import { TelegrafContext } from 'telegraf/typings/context';

export default function help(ctx: TelegrafContext): void {
    ctx.replyWithHTML('<b>/stop</b> for stoping search');
}
