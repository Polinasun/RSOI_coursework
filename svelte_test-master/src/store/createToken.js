import { writable } from 'svelte/store';
import {USERS_ENDPOINT} from '../services/api'

export default function createToken(tokenType) {
	const { subscribe, set } = writable(null, (set) => {
        const accessToken = localStorage.getItem('accessToken');
        if(accessToken) {
            const refreshToken = localStorage.getItem('refreshToken');
            const accessTokenValidUntil = localStorage.getItem('accessTokenValidUntil');
            const refreshTokenValidUntil = localStorage.getItem('refreshTokenValidUntil');
            set({accessToken, refreshToken, accessTokenValidUntil, refreshTokenValidUntil});
        }
    });

	return {
		subscribe,
		signUp: async (credits) => {
            const response = await fetch(`${USERS_ENDPOINT}/auth/`, {
                method: 'POST',
                body: JSON.stringify(credits)
            });
            const result = await response.json();
            if(response.status !== 400) {
                const {data: {
                    access_token: accessToken,
                    refresh_token: refreshToken,
                    access_token_valid_until: accessTokenValidUntil,
                    refresh_token_valid_until: refreshTokenValidUntil
                }} = result;

                localStorage.setItem('accessToken', accessToken);
                localStorage.setItem('refreshToken', refreshToken);
                localStorage.setItem('accessTokenValidUntil', accessTokenValidUntil);
                localStorage.setItem('refreshTokenValidUntil', refreshTokenValidUntil);
                set({accessToken, refreshToken, accessTokenValidUntil, refreshTokenValidUntil});
            } else {
                set(null);
                const {message} = result;
                throw {message};
            }
        },
		refreshToken: async (credits) => {
            const refreshToken = localStorage.getItem('refreshToken');
            const response = await fetch(`${USERS_ENDPOINT}/auth/`, {
                method: 'POST',
                body: JSON.stringify({refresh_token: refreshToken})
            });
            const result = await response.json();
            if(response.status !== 400) {
                console.log('result', result);
                const {data: {
                    access_token: accessToken,
                    refresh_token: refreshToken,
                    access_token_valid_until: accessTokenValidUntil,
                    refresh_token_valid_until: refreshTokenValidUntil
                }} = result;
                localStorage.setItem('accessToken', accessToken);
                localStorage.setItem('refreshToken', refreshToken);
                localStorage.setItem('accessTokenValidUntil', accessTokenValidUntil);
                localStorage.setItem('refreshTokenValidUntil', refreshTokenValidUntil);
                set({accessToken, refreshToken, accessTokenValidUntil, refreshTokenValidUntil});
                return accessToken;
            } else {
                set(null);
                const {message} = result;
                throw {message};
            }
        },
		logout: () => {
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            localStorage.removeItem('accessTokenValidUntil');
            localStorage.removeItem('refreshTokenValidUntil');
            set(null);
        }
	};
}