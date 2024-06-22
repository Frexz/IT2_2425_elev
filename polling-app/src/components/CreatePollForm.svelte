<script>
    import Button from '../shared/Button.svelte'

    let fields = { question: '', answerA: '', answerB: '' }
    let errors = { question: '', answerA: '', answerB: '' }
    let valid = false

    const handleSubmit = () => {
        valid = true

        if (fields.question.trim().length < 5) {
            valid = false
            errors.question = 'Question must be at least 5 characters long.'
        } else {
            errors.question = ''
        }

        if (fields.answerA.trim().length < 1) {
            valid = false
            errors.answerA = 'Answer A cannot be empty.'
        } else {
            errors.answerA = ''
        }

        if (fields.answerB.trim().length < 1) {
            valid = false
            errors.answerB = 'Answer B cannot be empty.'
        } else {
            errors.answerB = ''
        }

        if (valid) {
            console.log('valid', fields);
        }
    }
</script>

<form on:submit|preventDefault={handleSubmit}>
    <div class="form-field">
        <label for="question">Poll Question</label>
        <input type="text" id="question" bind:value={fields.question}>
        <div class="error">{errors.question}</div>
    </div>
    <div class="form-field">
        <label for="answer-a">Answer A:</label>
        <input type="text" id="answer-a" bind:value={fields.answerA}>
        <div class="error">{errors.answerA}</div>
    </div>
    <div class="form-field">
        <label for="answer-b">Answer B:</label>
        <input type="text" id="answer-b" bind:value={fields.answerB}>
        <div class="error">{errors.answerB}</div>
    </div>
    <Button type='secondary' flat={true}>Add Poll</Button>
</form>

<style>
    form {
        width: 400px;
        margin: 0 auto;
        text-align: center;
    }

    .form-field {
        margin: 18px auto;
        text-align: left;
    }

    input {
        width: 100%;
        border-radius: 4px;
        height: 24px;
        border: 1px solid #ddd;
    }

    label {
        margin: 10px auto;
        text-align: left;
    }

    .error {
        font-weight: bold;
        font-size: 12px;
        color: #d91b42;
    }
</style>