<script>
    let people = [
        { name: 'Yoshi', beltColor: 'green', age: 25, id: 1},
        { name: 'Mario', beltColor: 'orange', age: 45, id: 2},
        { name: 'Luigi', beltColor: 'black', age: 35, id: 3},
    ]

    const handleClick = (id) => {
        people = people.filter((person) => person.id != id)
    }
</script>

<main>
    {#each people as person (person.id)}
        <div class="person">
            <h4>{person.name}</h4>
            <p>{person.age} years old, {person.beltColor} belt.</p>
            <button on:click={() => handleClick(person.id)}>Delete</button>
        </div>
    {:else}
        <p>There are no people to show ...</p>
    {/each}
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center
    }

    .person {
        display: flex;
        flex-direction: column;
    }
</style>