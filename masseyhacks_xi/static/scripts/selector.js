let URL_KINDS = {
    song: "single",
    album: "album"
}

async function fetchResults(data) {
    if (data.searchValue == "") {
        return;
    }
    try {
        data.isLoading = true;
        const response = await fetch(
            "/selector/search?" +
                new URLSearchParams({
                    kind: data.searchKind,
                    value: data.searchValue,
                })
        );
        if (!response.ok) {
            data.isLoading = false;
            throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        data.isLoading = false;
        return json;
    } catch (error) {
        data.isLoading = false;
        console.error(error.message);
    }
}
