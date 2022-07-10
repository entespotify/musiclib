import Home from '../../home/static/js/home';

class Initializer {
    routes() {
        return [
            {
                domElement: 'home',
                module: Home
           }
        ];
    }

    constructor() {
        var self = this;

        // if (typeof IHG_Page != 'undefined') {
        //     let util = new Util(IHG_Page);
        //     let services = new Services(IHG_Page);
        // }

        /*------------------------------------------------------------------
         * MutationObserver is used to listen for DOM changes
         * DOC: https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver#Instance_methods
         * Performance related article : https://hacks.mozilla.org/2012/05/dom-mutationobserver-reacting-to-dom-changes-without-killing-browser-performance/
         *------------------------------------------------------------------
         */

        // observe body element for mutations change
        var targetNode = document.querySelector('body');

        // Options for the observer (which mutations to observe)
        var config = { attributes: true, childList: true, subtree: true };

        // Callback function to execute when mutations are observed
        let callback = function (mutationsList) {
            for (var mutation of mutationsList) {
                if (mutation.type == 'childList') {
                    let newNodes = mutation.addedNodes;
                    // if new nodes are added to the DOM run through initialize component code
                    if (newNodes.length) {
                        newNodes.forEach((element) => {
                            self.initComponent(element);
                        });
                    }
                }
            }
        };

        if (targetNode) {
            let observer = new MutationObserver(callback);

            // Start observing on body element for configured mutations
            observer.observe(targetNode, config);
        }
        this.initComponent();
    }

    initComponent(scope) {
        var _scope = typeof scope == 'undefined' ? document : scope;
        this.routes().forEach((route) => {
            if (_scope && _scope.querySelectorAll) {
                var componentReferences = _scope.querySelectorAll(
                    `[data-component-${route.domElement}]`
                );
                if (componentReferences.length) {
                    componentReferences.forEach((element) => {
                        let mod = new route.module(element);
                    });
                }
            }
        });
    }
}

export { Initializer };