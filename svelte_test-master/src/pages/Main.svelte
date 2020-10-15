<script>
    import { Nav } from "svelte-chota";
    import Accounts from "./Accounts.svelte";
    import Clubs from "./Clubs.svelte";
    import Couples from "./Couples.svelte";
    import Members from "./Members.svelte";
    import Referees from "./Referees.svelte";
    import Competitions from "./Competitions.svelte";
    import Competitors from "./Competitors.svelte";
    import Logout from "../components/Logout.svelte";
	import {router, Router, Route, Link } from 'yrv';
    
    const tabs = {
        "/users": {name: "Пользователи", component: Accounts},
        "/clubs": {name: "Клубы", component: Clubs},
        "/couples": {name: "Пары", component: Couples},
        "/competitions": {name: "Соревнования", component: Competitions},
        "/members/:club": {component: Members},
        "/referees/:comp": {component: Referees},
        "/competitors/:comp": {component: Competitors}
    };
</script>
<div>
    {#if tabs[$router.path]}
        <Nav>
            <a slot="left" href="/" class="brand">DANCE</a>
            <div class="main-menu-links" slot="left">
                {#each Object.entries(tabs) as [url, {name}]}
                    {#if name}
                        <Link class={$router.path === url ? "active" : ""} href={url}>{name}</Link>
                    {/if}
                {/each}
            </div>
            <div slot="right">
                <Logout/>
            </div>
        </Nav>
    {/if}
</div>
<main>
    <Router>
        {#each Object.entries(tabs) as [url, {component}]}
            <Route path={url} component={component}/>
        {/each}
        <Route exact path="/test">Hello World</Route>
        <Route fallback=>Not found</Route>
    </Router>
</main>

<style>
    main {
        height: calc(100vh - 60px);
    }
    .main-menu-links {
        display: flex;
    }
</style>