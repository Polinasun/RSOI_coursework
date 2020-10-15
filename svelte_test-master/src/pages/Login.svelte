<script>
import { Container, Card, Button, Field, Input, Tag, Icon} from "svelte-chota";
import { Wave } from 'svelte-loading-spinners'
import { fade } from 'svelte/transition';
import { tokenStore } from "../store";

let login = '';
let password = '';
let loginPromise;

</script>
<form class="login-container"
    on:submit|preventDefault={() => {loginPromise = tokenStore.signUp({login, password})}}
>
    <Card class="login-card" style="min-width: 400px;">
        <h1 transition:fade slot="header">Авторизация</h1>
        <div transition:fade 
            class="login-form"
        >
            <Field>
                <Input bind:value={login} placeholder="login"/>
                <Input bind:value={password} password placeholder="password"/>
            </Field>
            {#await loginPromise}
                <div style="text-align: center">
                    <Wave size="60" color="#FF3E00" unit="px"/>
                </div>
            {:catch error}
                <Card class="text-error bd-error">{error.message}</Card>
            {/await}
        </div>
        <div slot="footer" class="is-right">
            <button
                type="submit"
                transition:fade
                class="button primary">
                Вход
            </button>
        </div>
    </Card>
</form>

<style>
    .login-container {
        display: flex;
        flex-direction: row;
        height: 70vh;
        justify-content: center;
        align-items: center;
        
    }
    .progress {
        animation: spin 4s linear infinite;
    }
    .login-form {
        padding: 30px 0;
    }
</style>