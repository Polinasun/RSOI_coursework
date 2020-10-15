import apiFetch from "../../services/apiFetch";
import {USERS_ENDPOINT} from "../../services/api";
const getDataErrors = (data) => {
    return data.reduce((obj, item) => {
        Object.entries(item).map(([key, value]) => {
            obj[key] = value;
        });
        return obj;
    }, {});
};

export const post = async (setErrors, { detail: { values, setSubmitting, resetForm } }) => {
    try {
        setErrors({});
        setSubmitting(true);
        const result = await apiFetch.post(`${USERS_ENDPOINT}/accounts/`, {
            withAuth: false,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(values)
        });
        if(result.statusCode === 400) {
            if(result.data) {
                setErrors(getDataErrors(result.data));
            } else {
                setErrors(result);
            }
        } else {
            resetForm();
        }
    } catch(err) {
        setErrors(err);
    } finally {
        setSubmitting(false);
    }
}

export const patch = async (id, setErrors, { detail: { values, setSubmitting, resetForm } }) => {
    console.log("patch sending", id, setErrors, values);
    try {
        setErrors({});
        setSubmitting(true);
        const result = await apiFetch.patch(`${USERS_ENDPOINT}/account/${id}/`, {
            withAuth: false,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(values)
        });
        if(result.statusCode === 400) {
            if(result.data) {
                setErrors(getDataErrors(result.data));
            } else {
                setErrors(result);
            }
        } else {
            resetForm();
        }
    } catch(err) {
        setErrors(err);
    } finally {
        setSubmitting(false);
    }
}

export const fetch = async (id, setData) => {
    const result = await apiFetch.get(`${USERS_ENDPOINT}/account/${id}/`);
    setData && setData(result);
}

export const deleteAct = async (id) => {
    await apiFetch.delete(`${USERS_ENDPOINT}/account/${id}/`);
}