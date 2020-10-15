<script>
    import { Form, Input, Select } from 'sveltejs-forms';
    import schema from './editSchema.js'
    export let initialValues = {};
    export let handleSubmit = () => {};
    export let handleCancel = () => {};
    let errors={};
    const setErrors = (err) => errors = err;
    const roleOpts = [
        {id: 'sportsman', title: 'Sportsman'},
        {id: 'trainer', title: 'Trainer'}
    ];
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
        name="login"
        label="Логин"
        placeholder="Логин" />
    {#if errors["login"] && touched["login"]}
        <div class="message">{errors["login"]}</div>
    {/if}
    <label>Роль</label>
    <Select
        name="role"
        options={roleOpts} />
    {#if errors["role"] && touched["role"]}
        <div class="message">{errors["role"]}</div>
    {/if}
    <button type="reset">Отмена</button>
    <button type="submit">Отправить</button>
</Form>

<style>
</style>