export async function load({ fetch, params }) {
    const id = params.id
    const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`)
    const guide = await res.json()

    if (res.ok) {
        return {
            guide
        }
    }

    return {
        status: res.status,
        error: new Error('Could not fetch the guide')
    }
}