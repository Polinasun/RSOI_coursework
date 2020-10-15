<script>
    import {Container, Card, Nav, Button, Field, Input, Modal} from "svelte-chota";
    import { onMount } from 'svelte';
    import { Circle2 } from 'svelte-loading-spinners'
    import VirtualList from '@sveltejs/svelte-virtual-list'
    import { fade } from 'svelte/transition';

    import Form from "../forms/referees/Form.svelte";
    import {post, deleteAct} from "../forms/referees/actions.js";
    import apiFetch from "../services/apiFetch";
    import {DANCERS_ENDPOINT} from "../services/api";

    import {delay} from "../services/utils";
    export let uuid;
    let promise = {};
    const fetch = () => {
        promise = {};
        promise = apiFetch.get(`${DANCERS_ENDPOINT}/sportsman/${uuid}/`, {withAuth: false})
            .then(result => {
                if(result.statusCode === 400) {
                    throw result;
                }
                return result;
            });
    };
    fetch();
</script>
<Container style="height: 80vh;">
    {#await promise then result}
        <Card style="margin: 10px" class="item">
            <div slot="header">
                <h3>{result.data[0].first_name} {result.data[0].patronymic}</h3>
                <span class="text-grey">Ранг: {result.data[0].referee_rank}</span>
            </div>
            <div class="is-right">
                <slot name="controls"/>
            </div>         
        </Card>
    {/await}
</Container>
