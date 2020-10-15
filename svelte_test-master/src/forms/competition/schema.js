import * as yup from 'yup';
export const shape = {
    name: yup.string().required(),
    age_group: yup.string().required(),
    rank: yup.string().required()
};
const regSchema = yup.object().shape(shape);

export default regSchema;