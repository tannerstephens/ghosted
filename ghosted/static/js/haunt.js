function download_ghosts() {
  document.getElementById('filedownload').src = '/haunt/download?r=' + Math.random();
}


function update_ghosts(ghosts) {
  const ghost_id = document.getElementById("uid").innerHTML;
  const ghostIconURL = document.getElementById('ghost').innerHTML;
  const ghostOIconURL = document.getElementById('ghost-o').innerHTML;

  const nodes = new vis.DataSet(ghosts.reduce(function(acc, cur) {
    if (cur.is_active) {
      acc.push({
        id: cur.id,
        image: ghost_id == String(cur.id) ? ghostOIconURL : ghostIconURL,
        size: (cur.children.length*3 + 20),
        shape: 'image',
        color: {
          border: '#999'
        }
      });
    }

    return acc;
  }, []));


  const edges = new vis.DataSet(ghosts.reduce(function(acc, cur) {
    return acc.concat(cur.children.map(function(child) {
      return {
        from: cur.id,
        to: child.id,
        arrows: 'to'
      };
    }));
  }, []));

  const netdata = {
    nodes: nodes,
    edges: edges
  };

  const options = {};

  const container = document.getElementById("ghostView");

  const network = new vis.Network(container, netdata, options);
}


document.addEventListener('DOMContentLoaded', function() {
  const ghosts = JSON.parse(document.getElementById('ghosts').innerHTML);

  update_ghosts(ghosts);
})
