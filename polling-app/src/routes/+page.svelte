<script>
    import Header from '../components/Header.svelte'
    import Footer from '../components/Footer.svelte'
    import Tabs from '../shared/Tabs.svelte'

    let items = ['Current Polls', 'Add New Poll']
    let activeItem = 'Current Polls'

    const handleTabChange = (e) => {
        activeItem = e.detail
    }
</script>

<Header />
<main>
    <Tabs {items} {activeItem} on:tabChange={handleTabChange} />
    {#if activeItem === 'Current Polls'}
        <p>Poll list component goes here</p>
    {:else if activeItem === 'Add New Poll'}
        <p>New poll form component goes here</p>
    {/if}
</main>
<Footer />

<style>
    main {
        max-width: 960px;
        margin: 40px auto;
    }

    :global(body) {
        margin: 0;
    }
</style>