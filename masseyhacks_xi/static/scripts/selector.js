async function fetchResults({ searchKind, searchValue }) {
    try {
        const response = await fetch(
            "/selector/search?" +
                new URLSearchParams({
                    kind: searchKind,
                    value: searchValue,
                })
        );
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        return json;
    } catch (error) {
        console.error(error.message);
    }
}
