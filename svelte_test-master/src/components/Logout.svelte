<script>
import { Button } from "svelte-chota";
import { tokenStore } from "../store";

</script>
<a href="#" class="text-secondary" secondary small on:click={() => tokenStore.logout()}>Выход</a>
<style>
</style>