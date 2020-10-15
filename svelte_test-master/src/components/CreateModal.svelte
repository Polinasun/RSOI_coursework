<script>
    import { Modal,Button,Card } from 'svelte-chota';
    export let submit;
    export let createForm;
    let form;
    let open = false;
    const show = () => open=true;
    const hide = () => {
        form.reset();
        open=false;
    }
    const handleSubmit = async () => {
        await submit();

    }
</script>

<Button on:click={show}>Add</Button>
<Modal bind:open>
    <Card>
        <form bind:this={form} on:submit={submit}>
            <div slot="footer" class="is-right">
                <Button clear on:click={hide}>Отмена</Button>
                <Button primary>Создать</Button>
            </div>
        </form>
    </Card>
</Modal>