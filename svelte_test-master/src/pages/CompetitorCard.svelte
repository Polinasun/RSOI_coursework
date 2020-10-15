<script>
    import {Container, Card, Nav, Button, Field, Input, Modal} from "svelte-chota";
    import { onMount } from 'svelte';
    import { Circle2 } from 'svelte-loading-spinners'
    import VirtualList from '@sveltejs/svelte-virtual-list'
    import { fade } from 'svelte/transition';

    import Form from "../forms/referees/Form.svelte";
    import {post, deleteAct} from "../forms/referees/actions.js";
    import apiFetch from "../services/apiFetch"
    import CoupleCard from "./CoupleCard.svelte";
    import {DANCERS_ENDPOINT} from "../services/api";

    import {delay} from "../services/utils";
    export let uuid;
    alert('uuid: ', uuid);
    let promise = {};
    const fetch = () => {
        promise = {};
        promise = apiFetch.get(`${DANCERS_ENDPOINT}/couple/${uuid}/`, {withAuth: false})
            .then(result => {
                if(result.statusCode === 400) {
                    throw result;
                }
                return result;
            });
    };

    fetch();
</script>
{#await promise then result}
    <CoupleCard male={result.data[0].male} female={result.data[0].female}>
        <div slot="controls"><slot name="controls"/></div>
    </CoupleCard>
{/await}
    
