import moment from 'moment'
import {tokenStore} from "../store"

async function withAuthHeaders(headers) {

    const accessToken = localStorage.getItem('accessToken');
    const refreshToken = localStorage.getItem('refreshToken');
    const accessTokenValidUntil = localStorage.getItem('accessTokenValidUntil');
    const refreshTokenValidUntil = localStorage.getItem('refreshTokenValidUntil');
    console.log("token is norma", accessTokenValidUntil, moment(accessTokenValidUntil, 'DD/MM/YY HH:mm:ss').valueOf(), Date.now())
    if(accessToken && moment(accessTokenValidUntil, 'DD/MM/YY HH:mm:ss').valueOf() > Date.now()) {
        return {...headers, authorization: accessToken}
    } else if(refreshToken && moment(refreshTokenValidUntil, 'DD/MM/YY HH:mm:ss').valueOf() > Date.now()) {
        const accessToken = await tokenStore.refreshToken();
        return {...headers, authorization: accessToken}
    }
    tokenStore.logout();
    return headers;
}
async function customFetch(url, {withAuth = true, headers: customHeaders = {}, ...props}) {
    const headers = withAuth ? await withAuthHeaders(customHeaders) : customHeaders;
    console.log('headers', headers)
    const response = await fetch(url, {headers, ...props});
    const result =  await response.json();
    result.statusCode = response.status;
    return result;
}
const createApiFetch = () => (
    {
        post(url, props={}) {
            return  customFetch(url, {method: 'POST', ...props})
        },
        get(url, props={}) {
            return  customFetch(url, {method: 'GET', ...props})
        },
        patch(url, props={}) {
            return  customFetch(url, {method: 'PATCH', ...props})
        },
        delete(url, props={}) {
            return  customFetch(url, {method: 'DELETE', ...props})
        },
        options(url, props={}) {
            return  customFetch(url, {method: 'OPTIONS', ...props})
        }
    }
);

export default createApiFetch();