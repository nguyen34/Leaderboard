#! /bin/bash

fn_info() {
    echo "Kubernetes Cluster"
}

declare -a processed_optional_args
fn_get_run_args() {
    count=0
    while test $# -gt 0
    do
        case "$1" in
            --no-deps)
                processed_optional_args="--no-deps $processed_optional_args"
                ((count=count + 1))
                ;;
            --user)
                processed_optional_args="--user $2 $processed_optional_args"
                ((count=count + 2))
                shift
                ;;
            *)
                break
                ;;
        esac
        shift
    done

    return $count
}


fn_frontend() {
    fn_get_run_args $@
    count=$?
    while test $count -gt 0; do ((count=count - 1)); shift; done

    cd frontend
    npm install

    case $1 in
        build)
            npm run build
            ;;

        start|run)
            npm run dev
            ;;
        test)
            npm run test
            ;;
        *)
            echo "Unknown command"
            ;;
    esac
}


fn_backend() {
    fn_get_run_args $@
    count=$?
    while test $count -gt 0; do ((count=count - 1)); shift; done
    
    cd backend
    case $1 in
        env)
            source .env/bin/activate
            ;;
        run|start)
            python manage.py runserver
            ;;
        startapp)
            python manage.py startapp $2
            ;;
        migrate)
            python manage.py migrate
            ;;
        makemigrations)
            python manage.py makemigrations
            ;;
        *)
            echo "Unknown command"
            ;;
    esac
}

arg=$1
shift
case $arg in
    info)
        fn_info
        ;;
    f|front|frontend)
        fn_frontend $@
        ;;

    b|back|backend)
        fn_backend $@
        ;;
    *) 
        echo "Unknown command"
        ;;
esac