import { Markup } from 'telegraf';
import { TelegrafContext } from 'telegraf/typings/context';

const cards: Array<string> = [
    'BMW', 'Audi', 'Ford', 'Dodge'
];

export default function({ reply }: TelegrafContext): void {
    reply(
        'Okey. Select brands',
        Markup.inlineKeyboard(cards.map(car => Markup.callbackButton(car, car))).extra()
    );
};
