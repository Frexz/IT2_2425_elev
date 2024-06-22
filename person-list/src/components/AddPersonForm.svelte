<script>
    import { createEventDispatcher } from "svelte"

    let dispatch = createEventDispatcher()

    let name
    let beltColor
    let age
    let skills = []

    const handleSubmit = () => {
        const person = {
            name,
            beltColor,
            age,
            skills,
            id: Math.random()
        }

        dispatch('addPerson', person)
    }

</script>

<h4>Add a New Person</h4>
<form on:submit|preventDefault={handleSubmit}>
    <input type="text" placeholder="Enter a name ..." bind:value={name}>
    <input type="number" placeholder="Enter an age ..." bind:value={age}>
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>Skills:</label>
    <div class="checkboxes">
        <input type="checkbox" bind:group={skills} value="fighting">Fighting <br>
        <input type="checkbox" bind:group={skills} value="sneaking">Sneaking <br>
        <input type="checkbox" bind:group={skills} value="running">Running <br>
    </div>
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>Belt Color:</label>
    <select bind:value={beltColor}>
        <option value="black">Black</option>
        <option value="orange">Orange</option>
        <option value="brown">Brown</option>
        <option value="white">White</option>
    </select>
    <button>Add Person</button>
</form>

<style>
    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
    }

    .checkboxes {
        display: inline;
    }
</style>