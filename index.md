---
permalink: /
title: Glosario
---
<p>
  <code>glosario</code> is an open source glossary of terms used in data science
  that is available online and also as a library in both
  <a href="https://github.com/carpentries/glosario-r/">R</a>
  and
  <a href="https://github.com/carpentries/glosario-py/">Python</a>.
  By adding glossary keys to a lesson's metadata, authors can indicate what the
  lesson teaches, what learners ought to know before they start, and where they
  can go to find that knowledge.  Authors can also use the library's functions
  to insert consistent hyperlinks for terms and definitions in their lessons in
  any of several (human) languages.
</p>

{% for lang in site.languages %}
  {% assign link = lang.key | prepend: './' | append: '/' | relative_url %}
  {% assign flag = './static/flags/' | append: lang.flag | append: '.svg' | relative_url %}
  <p>
    <a href="{{link}}">
      <img class="flag" src="{{flag}}" alt="{{lang.name}}">
    </a>
    <a href="{{link}}">{{lang.name}}</a>
  </p>
{% endfor %}
