(function(){
    var jquery_version = '3.4.1'
    var site_url = '127.0.0.1:800/'
    var min_height  = 100
    var min_width  = 100


    function bookmarklet(msg){

        //here goes the bookmarklet code
        var css =   jQuery('<link>')
        ccs.attr({
            rel : 'stylesheet',
            type: 'text/css',
            href: '{%static "styles.css"%}'
        })

    }
    if (typeof window.jQuery !=='undefined'){
        bookmarklet();
    }
    else{
        var conflict =  typeof window.$ != 'undefined'
        var script =document.createElement('script')
        script.src = '//ajax.googleapis.com/ajax/libs/jquery/' + jquery_version  + '/jquery.min.js'
        document.head.appendChild(script)
        var attempts  = 15;
        (function(){
            if (typeof window.jQuery =='undefined'){
                if( --attempts > 0){
                    window.setTimeout(arguments.callee , 250)

                }
                else{
                    alert('an occured while loading jquery')
    
            }

        }else{
            bookmarklet();
        }


        })()

    }
     
})()