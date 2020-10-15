import * as yup from 'yup';
export const shape = {
    referee_uuid: yup.string()
};
const regSchema = yup.object().shape(shape);

export default regSchema;