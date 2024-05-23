async function postEmailNickname() {
    cleanHistoryContainer();
    
    await fetch('http://localhost:80/emails/nickname', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "text": document.getElementById("textInput").value })
    }).then(res => {
        if (!res.ok) {
            document.getElementById("output").innerText = "";
            switch(res.status) {
                case 400:
                    document.getElementById("error").innerText = "JSON parse error";
                    break;
                case 422:
                    document.getElementById("error").innerText = "Недопустимые параметры запроса";
                    break;
                case 404:
                    document.getElementById("error").innerText = "Страница не найдена";
                    break;
            }
        } else {
            console.log(res);
            let data = res.json()
            console.log(data);
    
            document.getElementById("error").innerText = "";
            data.then(
                res => document.getElementById("output").innerText = `Никнейм пользователя: ${res.nickname} `
            )
        }
    })
}

async function postEmailDomain() {
    cleanHistoryContainer();
    await fetch('http://localhost:80/emails/domain', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "text": document.getElementById("textInput").value })
    }).then(res => {
        if (!res.ok) {
            document.getElementById("output").innerText = "";
            switch(res.status) {
                case 400:
                    document.getElementById("error").innerText = "JSON parse error";
                    break;
                case 422:
                    document.getElementById("error").innerText = "Недопустимые параметры запроса";
                    break;
                case 404:
                    document.getElementById("error").innerText = "Страница не найдена";
                    break;
            }
        } else {
            console.log(res);
            let data = res.json()
            console.log(data);
    
            document.getElementById("error").innerText = "";
            data.then(
                res => document.getElementById("output").innerText = `Домен пользователя: ${res.domain} `
            )
        }
    })
}



async function getHistoryNickname(page) {
    document.getElementById("error").innerText = "";
    document.getElementById("output").innerText = "";
    await fetch(`http://localhost:80/emails/nickname?page=${page}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        
    }).then(res => {
        if (!res.ok) {
            document.getElementById("output").innerText = "";
            switch(res.status) {
                case 422:
                    document.getElementById("error").innerText = "Недопустимые параметры запроса";
                    break;
                case 404:
                    document.getElementById("error").innerText = "Страница не найдена";
                    break;
            }
        } else {
            document.getElementById("output").innerText = "История никнеймов";
            let data = res.json();
            data.then(res => {
                console.log(res);
                createHistoryTable(res.nicknames);
                createPagination(Math.ceil(res.total / 5), "nickname")
            })
        }
    })

}

async function getHistoryDomain(page) {
    document.getElementById("error").innerText = "";
    document.getElementById("output").innerText = "";
    await fetch(`http://localhost:80/emails/domain?page=${page}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        
    }).then(res => {
        if (!res.ok) {
            document.getElementById("output").innerText = "";
            switch(res.status) {
                case 422:
                    document.getElementById("error").innerText = "Недопустимые параметры запроса";
                    break;
                case 404:
                    document.getElementById("error").innerText = "Страница не найдена";
                    break;
            }
        } else {
            let data = res.json();
            document.getElementById("output").innerText = "История доменов";
            data.then(res => {
                console.log(res);
                createHistoryTable(res.domains);
                createPagination(Math.ceil(res.total / 5), "domain")
            })
        }
    })
}

function createHistoryTable(dataArray) {
    let listContainer = document.getElementById('list-container');

    while (listContainer.firstChild) {
        listContainer.removeChild(listContainer.firstChild);
    }

    let table = document.createElement('table');
    for (let i = 0; i < dataArray.length; i++) {
        let tr = table.insertRow();
        tr.insertCell().appendChild(document.createTextNode((i + 1).toString()));
        tr.insertCell().appendChild(document.createTextNode(dataArray[i]));
    }
    listContainer.appendChild(table);
}


function createPagination(numberOfPages, type) {
    let paginationContainer = document.getElementById('pagination-container');
    while (paginationContainer.firstChild) {
        paginationContainer.removeChild(paginationContainer.firstChild);
    }

    for (let i = 1; i <= numberOfPages; i++) {
        let btn = document.createElement('button');
        btn.innerText = i;
        btn.onclick = function() {
            type === "nickname" ? getHistoryNickname(i) : getHistoryDomain(i);
        };
        paginationContainer.appendChild(btn);
    }
}


function cleanHistoryContainer() {
    let paginationContainer = document.getElementById('pagination-container');
    while (paginationContainer.firstChild) {
        paginationContainer.removeChild(paginationContainer.firstChild);
    }
    let listContainer = document.getElementById('list-container');

    while (listContainer.firstChild) {
        listContainer.removeChild(listContainer.firstChild);
    }
}

