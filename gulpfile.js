const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const del = require('del');
const rename = require('gulp-rename');
const webpack = require('gulp-webpack');
const concat = require('gulp-concat');
const uglify = require('gulp-uglify');

gulp.task('styles', () => {
    return gulp.src('./static/scss/main.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(rename("styles.css"))
        .pipe(gulp.dest('./static/dist/css/'));
});

gulp.task('clean', () => {
    return del([
        'static/dist/',
    ]);
});

gulp.task('watch', () => {
    gulp.watch('**/*.scss', (done) => {
        gulp.series(['clean', 'styles'])(done);
    });
});

// gulp.task('js', function() {
//     return gulp.src('./static/js/main.js')
//         .pipe(webpack())
//         .pipe(gulp.dest('./static/dist'));
// });
gulp.task('js', function () {
    return gulp.src('static/js/*.js')
        .pipe(uglify())
        .pipe(concat('script.js'))
        .pipe(gulp.dest('static/dist/js'));
});

gulp.task('default', gulp.series(['clean', 'styles', 'watch']));

gulp.task('build', gulp.series(['clean', 'styles', 'js']));
