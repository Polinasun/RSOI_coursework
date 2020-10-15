<script>
    import { Form, Input, Select, Choice } from 'sveltejs-forms';
    import schema from './schema.js'
    export let initialValues = {};
    export let handleSubmit = () => {};
    export let handleCancel = () => {};
    let errors={};
    const setErrors = (err) => errors = err;
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
    <Input
        name="name"
        label="Название"
        placeholder='Кубок им. Геннадия Андреевича Зюганова' />
    {#if errors["name"] && touched["name"]}
        <div class="message">{errors["name"]}</div>
    {/if}
    <Input
        name="age_group"
        label="Возрастная группа"
        placeholder='L1' />
    {#if errors["age_group"] && touched["age_group"]}
        <div class="message">{errors["age_group"]}</div>
    {/if}
    <Input
        name="rank"
        label="Ранг" />
    {#if errors["rank"] && touched["rank"]}
        <div class="message">{errors["rank"]}</div>
    {/if}
    <button type="reset">Отмена</button>
    <button type="submit">Отправить</button>
</Form>

<style>
</style>