<script>
    import {Container, Card, Nav, Button, Field, Input, Modal} from "svelte-chota";
    import { onMount } from 'svelte';
    import { Circle2 } from 'svelte-loading-spinners'
    import VirtualList from '@sveltejs/svelte-virtual-list'
    import { fade } from 'svelte/transition';

    import UserForm from "../forms/user/Form.svelte";
    import UserEditForm from "../forms/user/EditForm.svelte";
    import {post, patch, deleteAct} from "../forms/user/actions.js";
    import apiFetch from "../services/apiFetch";

    import {USERS_ENDPOINT} from "../services/api";
    import {delay} from "../services/utils";

    let isCreateModalOpen = false;
    let searchInputValue = "";
    let search = "";
    let acounts = [];
    let selected = null;

    let promise = {};
    const fetch = () => {
        promise = {};
        promise = apiFetch.get(`${USERS_ENDPOINT}/accounts/`)
            .then(result => {
                if(result.statusCode === 400) {
                    throw result;
                }
                return result;
            });
    };
    $: if(searchInputValue.length === 0 && search.length !== 0) {
        search = ""
    }
    $: console.log('selected', selected);
    const searchHandle = () => {search = searchInputValue.toLowerCase().trim()};
    fetch();
</script>
<Nav class="bg-light">
    <div class="search" slot="right">
        <form on:submit|preventDefault={searchHandle}>
            <Field gapless>
                <Input bind:value={searchInputValue} accessors placeholder="Search"/>
                <Button on:click={searchHandle} primary>Поиск</Button>
            </Field>
        </form>
    </div>
    <div class="search" slot="right">
        <Button dark on:click={e => {
            selected = null;
            isCreateModalOpen = true;
        }}>Добавить</Button>
    </div>
</Nav>
<Container style="height: 80vh;">
    <Modal bind:open={isCreateModalOpen}>
        <Card>
            {#if selected === null}
                <UserForm
                    handleCancel={e => isCreateModalOpen=false}
                    handleSubmit={(...args) => post(...args).then(delay(100)).then(fetch)}
                />
            {:else}
                <UserEditForm
                    initialValues={selected}
                    handleCancel={e => isCreateModalOpen=false}
                    handleSubmit={(...args) => patch(selected.uuid, ...args).then(delay(100)).then(fetch)}
                />
            {/if}
        </Card>
    </Modal>
    {#await promise}
        <div out:fade class='overflow'>
            <Circle2/>
        </div>
    {:then result}
        <div transition:fade style="height: 100%">
            <VirtualList items={(result.data || []).filter(({login=""}) => login.toLowerCase().indexOf(search.toLowerCase()) !== -1)} let:item>
                <Card style="margin: 10px" class="item">
                    <div slot="header">
                        <h3>{item.login}</h3>
                        <span class="text-grey">{item.role}</span>
                    </div>
                    <div class="is-right">
                        <Button on:click={e => {
                            selected = item;
                            isCreateModalOpen = true;
                        }} primary outline>Редактировать</Button>
                        <Button on:click={e => {deleteAct(item.uuid).then(delay(100)).then(fetch)}} outline>Удалить</Button>
                    </div>         
                </Card>
            </VirtualList>
        </div>
    {:catch error}
        <h1 sytle="align-self: center;" class="text-error">Ошибка получения списка пользователей</h1>
        <cite class="text-error">{error.message} </cite>
    {/await}
</Container>
<style>
    .search {
        margin-top: 5px;
        margin-bottom: -30px;
        margin-right: 10px;
    }
    .overflow {
        position: absolute;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background: #fff5;
    }
    cite::after {
        display: block;
        content: '!';
        font-size: 40pt;
    }
</style>