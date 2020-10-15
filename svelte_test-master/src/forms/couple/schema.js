import * as yup from 'yup';
export const shape = {
    female: yup.string().required(),
    male: yup.string().required()
};
const regSchema = yup.object().shape(shape);

export default regSchema;