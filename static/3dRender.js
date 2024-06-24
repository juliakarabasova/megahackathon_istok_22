const modelPath = "{% if product.model_3d %}{{ product.model_3d.url }}{% endif %}";
            const container = document.getElementById('model-viewer-container');
            const loader = new THREE.GLTFLoader();
            loader.load(modelPath, function(gltf) {
                const scene = new THREE.Scene();
                scene.background = new THREE.Color(0xEDEBEC);
                scene.add(gltf.scene);
                // Смещаем модель немного ниже и левее
                gltf.scene.position.y -= 1;
                gltf.scene.position.x -= 1;

                const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
                camera.position.z = 2.8;

                const renderer = new THREE.WebGLRenderer({ antialias: true });
                renderer.setSize(container.clientWidth, container.clientHeight);
                container.appendChild(renderer.domElement);

                const ambientLight = new THREE.AmbientLight(0x404040);
                scene.add(ambientLight);

                const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
                directionalLight.position.set(1, 1, 1);
                scene.add(directionalLight);

                const controls = new THREE.OrbitControls(camera, renderer.domElement);
                controls.enableDamping = true;
                controls.dampingFactor = 0.25;
                controls.enableZoom = true;
                controls.enablePan = true;
                controls.screenSpacePanning = false;
                controls.minDistance = 1;
                controls.maxDistance = 500;
                controls.maxPolarAngle = Math.PI / 2;

                function animate() {
                    requestAnimationFrame(animate);
                    controls.update();
                    renderer.render(scene, camera);
                }
                animate();
                window.addEventListener('resize', function() {
                    camera.aspect = container.clientWidth / container.clientHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(container.clientWidth, container.clientHeight);
                });
            }, undefined, function(error) {
                console.error(error);
            });