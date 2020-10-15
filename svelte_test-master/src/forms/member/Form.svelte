<script>
    import { Form, Input, Select, Choice } from 'sveltejs-forms';
    import schema from './schema.js'
    import {fetchDancers} from './actions.js'
    export let initialValues = {};
    export let handleSubmit = () => {};
    export let handleCancel = () => {};
    let errors={};
    const setErrors = (err) => errors = err;
    let dancerOpts = [];
    fetchDancers().then(({data}) => dancerOpts = data.map(({uuid, first_name, last_name}) => ({id: uuid, title: `${first_name} ${last_name}`})));
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
        options={dancerOpts}
        name="dancer"
        label="Танцор"
        placeholder='ТК "Лясин-трясин"' />
    {#if errors["dancer"] && touched["dancer"]}
        <div class="message">{errors["dancer"]}</div>
    {/if}
    <button type="reset">Отмена</button>
    <button type="submit">Отправить</button>
</Form>

<style>
</style>