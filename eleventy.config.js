module.exports = function (eleventyConfig) {
  // Static passthrough — copy these straight to the output folder as-is
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("src/styles.css");
  eleventyConfig.addPassthroughCopy("src/script.js");
  eleventyConfig.addPassthroughCopy("src/admin");

  // The Decap CMS entry page is plain static HTML (not a Nunjucks
  // template) — it's already handled by the passthrough copy above, so
  // tell Eleventy not to also try to process it as a page.
  eleventyConfig.ignores.add("src/admin/index.html");

  // So <img src="/assets/images/..."> paths work the same way they did
  // in the original plain-HTML version.
  eleventyConfig.addFilter("markdownInline", function (value) {
    // very small helper: allow *word* -> <em>word</em> in front-matter strings
    if (!value) return value;
    return value.replace(/\*(.+?)\*/g, "<em>$1</em>");
  });

  return {
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
  };
};
