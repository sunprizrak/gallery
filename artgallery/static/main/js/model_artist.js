scene = new THREE.Scene();
camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 180;
camera.position.y = 40;

renderer = new THREE.WebGLRenderer({alpha: true, antialias: true});
renderer.setClearColor(0x000000, 0);
renderer.setSize(533, 391);

const container = document.getElementById('cap-right');
renderer.domElement.setAttribute("id", "Artist3DObj");
container.appendChild( renderer.domElement );

const aLight = new THREE.AmbientLight(0x404040, 2);
scene.add(aLight);

const pLight = new THREE.PointLight(0xFFFFFF, 2.5);
pLight.position.set(0, -3, 7)
scene.add(pLight);

let loader = new THREE.GLTFLoader();
let obj = null;
loader.load(path, function(gltf) {
    obj = gltf;
    obj.scene.scale.set(3, 3, 3);

    scene.add(obj.scene);
});

function animate() {
    requestAnimationFrame(animate);

    if(obj)
        obj.scene.rotation.y += 0.02;

    renderer.render(scene, camera);
}
animate();