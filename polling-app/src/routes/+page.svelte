<script>
    import Modal from '../components/Modal.svelte'
    import '../app.css'

    let showModal = false

    let people = [
        { name: 'Yoshi', beltColor: 'green', age: 25, id: 1},
        { name: 'Mario', beltColor: 'orange', age: 45, id: 2},
        { name: 'Luigi', beltColor: 'black', age: 35, id: 3},
    ]

    const toggleModal = () => {
        showModal = !showModal
    }

    const handleClick = (id) => {
        people = people.filter((person) => person.id != id)
    }
</script>

<Modal message="Hey, I am a prop value" {showModal} on:click={toggleModal}/>
<main>
    <button on:click|once={toggleModal}>Open Modal</button>
    {#each people as person (person.id)}
        <div class="person">
            <h4>{person.name}</h4>
            {#if person.beltColor === 'black'}
                <p><strong>MASTER NINJA</strong></p>
            {/if}
            <p>{person.age} years old, {person.beltColor} belt.</p>
            <button on:click={() => handleClick(person.id)}>Delete</button>
        </div>
    {:else}
        <p>There are no people to show ...</p>
    {/each}
</main>