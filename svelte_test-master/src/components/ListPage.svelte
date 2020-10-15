<script>
    import {onMount} from "svelte";
    import {Container, Nav} from "svelte-chota";
    export let data;
</script>
<Container>
    <Nav>
        <slot name="header"/>
    </Nav>
	{#each data as item}
        <slot {item}/>
	{/each}
</Container>
<style>
</style>