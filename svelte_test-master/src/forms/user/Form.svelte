<script>
    import { Form, Input, Select, Choice } from 'sveltejs-forms';
    import schema from './schema.js'
    export let initialValues = {};
    export let handleSubmit = () => {};
    export let handleCancel = () => {};
    let errors={};
    const setErrors = (err) => errors = err;
    const genderCh = [{id: 'М', title: 'М'}, {id: 'Ж', title: 'Ж'}];
    const groupOpts = [
        {id: 'дети-1', title: 'дети-1'},
        {id: 'дети-2', title: 'дети-2'},
        {id: 'юниоры-1', title: 'юниоры-1'},
        {id: 'юниоры-2', title: 'юниоры-2'},
        {id: 'спорт высших достижений', title: 'спорт высших достижений'},
        {id: 'сеньоры', title: 'сеньоры'}
    ];
    const rankOpts = [
        {id: 'Нет', title: 'Нет'},
        {id: 'E', title: 'E'},
        {id: 'D', title: 'D'},
        {id: 'C', title: 'C'},
        {id: 'B', title: 'B'},
        {id: 'A', title: 'A'},
        {id: 'S', title: 'S'},
        {id: 'M', title: 'M'}
    ];
    const trOpts = [
        {id: 'Нет', title: 'Нет'},
        {id: 'Тренер', title: 'Тренер'},
        {id: 'Заслуженный тренер', title: 'Заслуженный тренер'}
    ];
    const refereeOpts = [
        {id: 'Нет', title: 'Нет'},
        {id: 'Юный спортивный судья', title: 'Юный спортивный судья'},
        {id: 'Спортивный судья 1-й категории', title: 'Спортивный судья 1-й категории'},
        {id: 'Спортивный судья 2-й категории', title: 'Спортивный судья 2-й категории'},
        {id: 'Спортивный судья 3-й категории', title: 'Спортивный судья 3-й категории'},
        {id: 'Спортивный судья всероссийской категории', title: 'Спортивный судья всероссийской категории'}
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
    <Input
        name="password"
        type="password"
        label="Пароль"
        placeholder="Пароль" />
    {#if errors["password"] && touched["password"]}
        <div class="message">{errors["password"]}</div>
    {/if}
    <Input
        name="first_name"
        label="Имя"
        placeholder="Иван" />
    {#if errors["first_name"] && touched["first_name"]}
        <div class="message">{errors["first_name"]}</div>
    {/if}
    <Input
        name="last_name"
        label="Фамилия"
        placeholder="Иванов" />
    {#if errors["last_name"] && touched["last_name"]}
        <div class="message">{errors["last_name"]}</div>
    {/if}
    <Input
        name="patronymic"
        label="Очество"
        placeholder="Ивнович" />
    {#if errors["patronymic"] && touched["patronymic"]}
        <div class="message">{errors["patronymic"]}</div>
    {/if}
    <Select
        label="Группа"
        name="age_group"
        options={groupOpts} />
    {#if errors["age_group"] && touched["age_group"]}
        <div class="message">{errors["age_group"]}</div>
    {/if}
    <Select
        label="Ранг"
        name="rank"
        options={trOpts} />
    {#if errors["rank"] && touched["rank"]}
        <div class="message">{errors["rank"]}</div>
    {/if}
    <Select
        label="Категория тренера"
        name="trainer_rank"
        options={trOpts} />
    {#if errors["trainer_rank"] && touched["trainer_rank"]}
        <div class="message">{errors["trainer_rank"]}</div>
    {/if}
        <Select
        label="Категория судьи"
        name="referee_rank"
        options={refereeOpts} />
    {#if errors["referee_rank"] && touched["referee_rank"]}
        <div class="message">{errors["referee_rank"]}</div>
    {/if}
    <label>Пол</label>
    <Choice
        name="gender"
        options={genderCh} />
    {#if errors["gender"] && touched["gender"]}
        <div class="message">{errors["logendergin"]}</div>
    {/if}
    <button type="reset">Отмена</button>
    <button type="submit">Отправить</button>
</Form>

<style>
</style>