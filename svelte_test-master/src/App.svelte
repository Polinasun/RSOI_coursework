<script>
	import Login from "./pages/Login.svelte";
	import Main from "./pages/Main.svelte";
	import { navigateTo, router, Router, Route, Link } from 'yrv';
	import {tokenStore} from "./store";

	$: if(!$tokenStore) {
		navigateTo('/auth')
	} else if($router.path === "/auth" || $router.path === "/") {
        console.log($router);
		navigateTo('/users')
	};
</script>

<Router>
	<Route disabled={!$tokenStore} component={Main}/>
	<Route exact path="/auth" component={Login}/>
</Router>

<style>
    :global(:root) {
        --color-primary: #f5ba25;
        --color-lightGrey: #d2d6dd;
        --color-grey: #747681;
        --color-darkGrey: #3f4144;
        --color-error: #d43939;
        --color-success: #28bd14;
        --grid-maxWidth: 120rem;
        --grid-gutter: 2rem;
        --font-size: 1.6rem;
		--font-family: "Helvetica Neue", sans-serif;
	}
    :global(input[type='checkbox'] + label) {
        display: inline-block;
        margin-right: 2rem;
    }

    :global(input[type='radio'] + label) {
        display: inline-block;
        margin-right: 2rem;
    }

    :global(.message) {
        font-size: 8pt;
        color: #888;
        margin: 5pt 10pt;
        color: #f56565;
    }

	cite {
        opacity: 0.8;
        margin-left: 10px;
        padding-left: 10px;
        font-size: 16pt;
        border-left: 3px solid;
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    cite::after {
        display: block;
        content: '"';
        font-size: 40pt;
    }
</style>