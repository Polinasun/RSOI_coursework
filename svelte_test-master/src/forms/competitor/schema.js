import * as yup from 'yup';
export const shape = {
    couple_uuid: yup.string()
};
const regSchema = yup.object().shape(shape);

export default regSchema;