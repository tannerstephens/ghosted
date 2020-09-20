window.onload = () => {
  const ghosts = JSON.parse(document.getElementById('ghosts').innerHTML);
  const ghostID = document.getElementById("uid").innerHTML;

  const nodes = new vis.DataSet(ghosts.reduce((acc, cur) => {
    const getGhostURL = ghostID => `/ghost/${ghostID}.png`;

    if (cur.is_active) {
      acc.push({
        id: cur.id,
        image: getGhostURL(cur.ghost_id),
        size: (cur.children.length*3 + 20),
        shape: 'image',
        color: {
          border: ghostID == String(cur.id) ? '#f58916' : '#999'
        }
      });
    }

    return acc;
  }, []));


  const edges = new vis.DataSet(ghosts.reduce((acc, cur) =>
    acc.concat(cur.children.map(child => ({
      from: cur.id,
      to: child.id,
      arrows: 'to'
    }))),
  []));

  const netdata = {
    nodes: nodes,
    edges: edges
  };

  const options = {};

  const container = document.getElementById("ghostView");

  new vis.Network(container, netdata, options);
}

const download_ghosts = () => {
  document.getElementById('filedownload').src = `/haunt/download?r=${Math.random()}`;
}
