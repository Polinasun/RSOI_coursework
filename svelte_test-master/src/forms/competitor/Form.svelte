<script>
    import { Form, Input, Select, Choice } from 'sveltejs-forms';
    import schema from './schema.js'
    import {fetchCouples} from './actions.js'
    export let initialValues = {};
    export let handleSubmit = () => {};
    export let handleCancel = () => {};
    let errors={};
    const setErrors = (err) => errors = err;

    let couplesOpts = [];
    fetchCouples().then(({data}) => couplesOpts = data.map(({uuid, first_name, last_name}) => ({id: uuid, title: `id: ${uuid}`})));
</script>

<Form
    {schema}
    {initialValues}
    validateOnBlur={false}
    validateOnChange={false}
    on:submit={handleSubmit.bind(this, setErrors)}
    on:reset={handleCancel.bind(this, setErrors)}
    let:isSubmitting
    let:isValid
    let:touched
>
    <Select
        options={couplesOpts}
        name="couple_uuid"
        label="ID пары" />
    {#if errors["couple_uuid"] && touched["couple_uuid"]}
        <div class="message">{errors["couple_uuid"]}</div>
    {/if}
    <button type="reset">Отмена</button>
    <button type="submit">Отправить</button>
</Form>

<style>
</style>