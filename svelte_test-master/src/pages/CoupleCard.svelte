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
    export let male;
    export let female;
    let femalePromise = {};
    const fetchFemale = () => {
        femalePromise = {};
        femalePromise = apiFetch.get(`${DANCERS_ENDPOINT}/sportsman/${male}/`, {withAuth: false})
            .then(result => {
                if(result.statusCode === 400) {
                    throw result;
                }
                return result;
            });
    };
    let malePromise = {};
    const fetchMale = () => {
        malePromise = {};
        malePromise = apiFetch.get(`${DANCERS_ENDPOINT}/sportsman/${female}/`, {withAuth: false})
            .then(result => {
                if(result.statusCode === 400) {
                    throw result;
                }
                return result;
            });
    };
    fetchFemale();
    fetchMale();
</script>
<Container style="height: 80vh;">
        <Card style="margin: 10px" class="item">
            <div slot="header">
            <h3>Пара</h3>
            {#await malePromise then result}
                <div class="text-grey">{result.data[0].first_name} {result.data[0].last_name}</div>
            {/await}
            {#await femalePromise then result}
                <div class="text-grey">{result.data[0].first_name} {result.data[0].last_name}</div>
            {/await}
            </div>
            <div class="is-right">
                <slot name="controls"/>
            </div>         
        </Card>
    
</Container>
