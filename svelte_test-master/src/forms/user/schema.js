import * as yup from 'yup';
export const shape = {
    login: yup.string().required(),
    password: yup.string(),
    first_name: yup.string().required(),
    last_name: yup.string().required(),
    patronymic: yup.string().required(),
    gender: yup.string().oneOf(['М', 'Ж']).required(),
    age_group: yup.string().oneOf(['L1', 'L2']),
    rank: yup.string().oneOf(['Нет','E', 'D', 'C', 'B', 'A', 'S', 'M']),
    trainer_rank: yup.string().oneOf([
        "Нет",
        'Тренер',
        'Заслуженный тренер'
    ]),
    referee_rank: yup.string().oneOf([
        'Нет', 
        'Юный спортивный судья', 
        'Спортивный судья 3-й категории',
        'Спортивный судья 3-й категории',
        'Спортивный судья 3-й категории',
        'Спортивный судья всероссийской категории'
    ]),
};
const regSchema = yup.object().shape(shape);

export default regSchema;