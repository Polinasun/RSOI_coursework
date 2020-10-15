import * as yup from 'yup';
export const shape = {
    login: yup.string().required(),
    role: yup.string().oneOf(['sportsman', 'trainer']).required()
};
const regSchema = yup.object().shape(shape);

export default regSchema;