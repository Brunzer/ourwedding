function ValidateEmail(a){
	var b=/^(.+)@(.+)$/;
	var c="(\"[^\"]*\")";
	var d=/^\[(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\]$/;
	var e="\[^\\s\\(\\)><@,;:\\\\\\\"\\.\\[\\]\]+";
	var f="("+e+"|"+c+")";
	var g=new RegExp("^"+f+"(\\."+f+")*$");
	var h=new RegExp("^"+e+"(\\."+e+")*$");
	var j=new RegExp("^"+e+"$");
	var k=a.match(b);
	if(k===null){
		return false
	}
	var l=k[1];
	var m=k[2];
	var i;
	for(i=0;i<l.length;i++){
		if(l.charCodeAt(i)>127){
			return false
		}
	}
	if(l.match(g)===null){
		return false
	}
	for(i=0;i<m.length;i++){
		if(m.charCodeAt(i)>127){
			return false
		}
	}
	var n=m.match(d);
	if(n!==null){
		for(i=1;i<=4;i++){
			if(n>255){
				return false
			}
		}
	}else{
		var o=m.split(".");
		var p=o.length;
		if(p<2){
			return false
		}
		for(i=0;i<p;i++){
			if(o[i].search(j)==-1){
				return false
			}
		}
	}
	return true
}

function ltrim(a,b){
	b=b||"\\s";
	return a.replace(new RegExp("^["+b+"]+","g"),"")
}

function rtrim(a,b){
	b=b||"\\s";
	return a.replace(new RegExp("["+b+"]+$","g"),"")
}

function checkEmail(a,b) {
    if (a != b)
    {
        return false;
    } else {
        return true;
    }
}