<script>
    import Modal from '../components/Modal.svelte'
    import AddPersonForm from '../components/AddPersonForm.svelte'
    import '../app.css'

    let showModal = false

    let people = [
        { name: 'Yoshi', beltColor: 'green', age: 25, id: 1, skills: ["Fighting"]},
    ]

    const toggleModal = () => {
        showModal = !showModal
    }

    const handleClick = (id) => {
        people = people.filter((person) => person.id != id)
    }

    const addPerson = (e) => {
        const person = e.detail
        people = [person, ...people]
        showModal = false
    }
</script>

<Modal  {showModal} on:click={toggleModal}>
   <AddPersonForm on:addPerson={addPerson}/>
</Modal>
<main>
    <button on:click={toggleModal}>Add Person</button>
    <div class="people">
        {#each people as person (person.id)}
            <div class="person" style="border: 3px solid {person.beltColor};">
                <h4>{person.name}</h4>
                {#if person.beltColor === 'black'}
                    <p><strong>MASTER NINJA</strong></p>
                {/if}
                <p>{person.age} years old</p>
                <p>{person.beltColor} belt</p>
                {#if person.skills}
                    <p>{person.skills}</p>
                {/if}
                <button on:click={() => handleClick(person.id)}>Delete</button>
            </div>
        {:else}
            <p>There are no people to show ...</p>
        {/each}
    </div>
</main>