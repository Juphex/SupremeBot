# Using NavigationDrawer for left navbar
https://github.com/kivy-garden/garden.navigationdrawer

# Code for Custom WebViewClient

```Java
package com.my.webview;

import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MyWebViewClient extends WebViewClient {
    private String script;

    public String getScript() {
        return this.script;
    }

    public void setScript(String script) {
        this.script = script;
    }

    @Override
    public void onPageFinished(WebView view, String url) {
        view.loadUrl(this.script);
    }
}
```
Referenced Library: android.jar (Android\Sdk\platforms\android-27\android.jar)
